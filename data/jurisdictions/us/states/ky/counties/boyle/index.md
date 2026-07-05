---
type: Jurisdiction
title: "Boyle County, KY"
classification: county
fips: "21021"
state: "KY"
demographics:
  population: 30941
  population_under_18: 6467
  population_18_64: 18701
  population_65_plus: 5773
  median_household_income: 61159
  poverty_rate: 15.64
  homeownership_rate: 67.95
  unemployment_rate: 5.8
  median_home_value: 209900
  gini_index: 0.4572
  vacancy_rate: 7.42
  race_white: 26082
  race_black: 2222
  race_asian: 282
  race_native: 0
  hispanic: 1457
  bachelors_plus: 7900
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9902
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.0064
  - to: "us/states/ky/districts/senate/12"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/house/54"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Boyle County, KY

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30941 |
| Under 18 | 6467 |
| 18–64 | 18701 |
| 65+ | 5773 |
| Median household income | 61159 |
| Poverty rate | 15.64 |
| Homeownership rate | 67.95 |
| Unemployment rate | 5.8 |
| Median home value | 209900 |
| Gini index | 0.4572 |
| Vacancy rate | 7.42 |
| White | 26082 |
| Black | 2222 |
| Asian | 282 |
| Native | 0 |
| Hispanic/Latino | 1457 |
| Bachelor's or higher | 7900 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 99% (congressional)
- [KY-06](/us/states/ky/districts/06.md) — 1% (congressional)
- [KY Senate District 12](/us/states/ky/districts/senate/12.md) — 100% (state senate)
- [KY House District 54](/us/states/ky/districts/house/54.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
