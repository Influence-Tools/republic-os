---
type: Jurisdiction
title: "Rich County, UT"
classification: county
fips: "49033"
state: "UT"
demographics:
  population: 2631
  population_under_18: 760
  population_18_64: 1316
  population_65_plus: 555
  median_household_income: 79009
  poverty_rate: 3.8
  homeownership_rate: 84.72
  unemployment_rate: 0.0
  median_home_value: 334600
  gini_index: 0.3561
  vacancy_rate: 72.64
  race_white: 2417
  race_black: 0
  race_asian: 2
  race_native: 21
  hispanic: 142
  bachelors_plus: 542
districts:
  - to: "us/states/ut/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ut/districts/senate/2"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ut/districts/house/4"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Rich County, UT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2631 |
| Under 18 | 760 |
| 18–64 | 1316 |
| 65+ | 555 |
| Median household income | 79009 |
| Poverty rate | 3.8 |
| Homeownership rate | 84.72 |
| Unemployment rate | 0.0 |
| Median home value | 334600 |
| Gini index | 0.3561 |
| Vacancy rate | 72.64 |
| White | 2417 |
| Black | 0 |
| Asian | 2 |
| Native | 21 |
| Hispanic/Latino | 142 |
| Bachelor's or higher | 542 |

## Districts

- [UT-01](/us/states/ut/districts/01.md) — 100% (congressional)
- [UT Senate District 2](/us/states/ut/districts/senate/2.md) — 100% (state senate)
- [UT House District 4](/us/states/ut/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
