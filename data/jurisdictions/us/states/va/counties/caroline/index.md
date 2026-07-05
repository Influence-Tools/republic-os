---
type: Jurisdiction
title: "Caroline County, VA"
classification: county
fips: "51033"
state: "VA"
demographics:
  population: 32098
  population_under_18: 7275
  population_18_64: 19469
  population_65_plus: 5354
  median_household_income: 87407
  poverty_rate: 11.25
  homeownership_rate: 82.35
  unemployment_rate: 5.26
  median_home_value: 307700
  gini_index: 0.4011
  vacancy_rate: 7.21
  race_white: 19782
  race_black: 7628
  race_asian: 339
  race_native: 96
  hispanic: 2464
  bachelors_plus: 6801
districts:
  - to: "us/states/va/districts/07"
    rel: in-district
    area_weight: 0.9925
  - to: "us/states/va/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/67"
    rel: in-district
    area_weight: 0.6227
  - to: "us/states/va/districts/house/66"
    rel: in-district
    area_weight: 0.3768
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Caroline County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32098 |
| Under 18 | 7275 |
| 18–64 | 19469 |
| 65+ | 5354 |
| Median household income | 87407 |
| Poverty rate | 11.25 |
| Homeownership rate | 82.35 |
| Unemployment rate | 5.26 |
| Median home value | 307700 |
| Gini index | 0.4011 |
| Vacancy rate | 7.21 |
| White | 19782 |
| Black | 7628 |
| Asian | 339 |
| Native | 96 |
| Hispanic/Latino | 2464 |
| Bachelor's or higher | 6801 |

## Districts

- [VA-07](/us/states/va/districts/07.md) — 99% (congressional)
- [VA Senate District 25](/us/states/va/districts/senate/25.md) — 100% (state senate)
- [VA House District 67](/us/states/va/districts/house/67.md) — 62% (state house)
- [VA House District 66](/us/states/va/districts/house/66.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
