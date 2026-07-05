---
type: Jurisdiction
title: "Magoffin County, KY"
classification: county
fips: "21153"
state: "KY"
demographics:
  population: 11348
  population_under_18: 2545
  population_18_64: 6646
  population_65_plus: 2157
  median_household_income: 33080
  poverty_rate: 38.16
  homeownership_rate: 75.41
  unemployment_rate: 9.02
  median_home_value: 89000
  gini_index: 0.4949
  vacancy_rate: 13.75
  race_white: 11038
  race_black: 12
  race_asian: 27
  race_native: 45
  hispanic: 104
  bachelors_plus: 1658
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/30"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/92"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Magoffin County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11348 |
| Under 18 | 2545 |
| 18–64 | 6646 |
| 65+ | 2157 |
| Median household income | 33080 |
| Poverty rate | 38.16 |
| Homeownership rate | 75.41 |
| Unemployment rate | 9.02 |
| Median home value | 89000 |
| Gini index | 0.4949 |
| Vacancy rate | 13.75 |
| White | 11038 |
| Black | 12 |
| Asian | 27 |
| Native | 45 |
| Hispanic/Latino | 104 |
| Bachelor's or higher | 1658 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 30](/us/states/ky/districts/senate/30.md) — 100% (state senate)
- [KY House District 92](/us/states/ky/districts/house/92.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
