---
type: Jurisdiction
title: "Amelia County, VA"
classification: county
fips: "51007"
state: "VA"
demographics:
  population: 13462
  population_under_18: 2716
  population_18_64: 7760
  population_65_plus: 2986
  median_household_income: 76717
  poverty_rate: 9.7
  homeownership_rate: 82.5
  unemployment_rate: 3.78
  median_home_value: 282400
  gini_index: 0.3861
  vacancy_rate: 6.84
  race_white: 9732
  race_black: 2627
  race_asian: 24
  race_native: 0
  hispanic: 528
  bachelors_plus: 2270
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.9952
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/va/districts/house/72"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Amelia County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13462 |
| Under 18 | 2716 |
| 18–64 | 7760 |
| 65+ | 2986 |
| Median household income | 76717 |
| Poverty rate | 9.7 |
| Homeownership rate | 82.5 |
| Unemployment rate | 3.78 |
| Median home value | 282400 |
| Gini index | 0.3861 |
| Vacancy rate | 6.84 |
| White | 9732 |
| Black | 2627 |
| Asian | 24 |
| Native | 0 |
| Hispanic/Latino | 528 |
| Bachelor's or higher | 2270 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 100% (state senate)
- [VA House District 72](/us/states/va/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
