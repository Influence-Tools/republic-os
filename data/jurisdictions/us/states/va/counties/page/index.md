---
type: Jurisdiction
title: "Page County, VA"
classification: county
fips: "51139"
state: "VA"
demographics:
  population: 23727
  population_under_18: 4661
  population_18_64: 13780
  population_65_plus: 5286
  median_household_income: 57037
  poverty_rate: 11.35
  homeownership_rate: 71.76
  unemployment_rate: 5.52
  median_home_value: 233200
  gini_index: 0.4315
  vacancy_rate: 17.1
  race_white: 21877
  race_black: 498
  race_asian: 94
  race_native: 37
  hispanic: 609
  bachelors_plus: 3619
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9947
  - to: "us/states/va/districts/senate/2"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/va/districts/house/33"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Page County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23727 |
| Under 18 | 4661 |
| 18–64 | 13780 |
| 65+ | 5286 |
| Median household income | 57037 |
| Poverty rate | 11.35 |
| Homeownership rate | 71.76 |
| Unemployment rate | 5.52 |
| Median home value | 233200 |
| Gini index | 0.4315 |
| Vacancy rate | 17.1 |
| White | 21877 |
| Black | 498 |
| Asian | 94 |
| Native | 37 |
| Hispanic/Latino | 609 |
| Bachelor's or higher | 3619 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 99% (congressional)
- [VA Senate District 2](/us/states/va/districts/senate/2.md) — 100% (state senate)
- [VA House District 33](/us/states/va/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
