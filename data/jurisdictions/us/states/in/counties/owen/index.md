---
type: Jurisdiction
title: "Owen County, IN"
classification: county
fips: "18119"
state: "IN"
demographics:
  population: 21604
  population_under_18: 4396
  population_18_64: 12606
  population_65_plus: 4602
  median_household_income: 62464
  poverty_rate: 12.34
  homeownership_rate: 81.36
  unemployment_rate: 2.99
  median_home_value: 172400
  gini_index: 0.4273
  vacancy_rate: 13.11
  race_white: 20583
  race_black: 180
  race_asian: 123
  race_native: 9
  hispanic: 333
  bachelors_plus: 3516
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/in/districts/senate/39"
    rel: in-district
    area_weight: 0.5224
  - to: "us/states/in/districts/senate/37"
    rel: in-district
    area_weight: 0.4775
  - to: "us/states/in/districts/house/46"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Owen County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21604 |
| Under 18 | 4396 |
| 18–64 | 12606 |
| 65+ | 4602 |
| Median household income | 62464 |
| Poverty rate | 12.34 |
| Homeownership rate | 81.36 |
| Unemployment rate | 2.99 |
| Median home value | 172400 |
| Gini index | 0.4273 |
| Vacancy rate | 13.11 |
| White | 20583 |
| Black | 180 |
| Asian | 123 |
| Native | 9 |
| Hispanic/Latino | 333 |
| Bachelor's or higher | 3516 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 39](/us/states/in/districts/senate/39.md) — 52% (state senate)
- [IN Senate District 37](/us/states/in/districts/senate/37.md) — 48% (state senate)
- [IN House District 46](/us/states/in/districts/house/46.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
