---
type: Jurisdiction
title: "Nelson County, VA"
classification: county
fips: "51125"
state: "VA"
demographics:
  population: 14732
  population_under_18: 2564
  population_18_64: 7809
  population_65_plus: 4359
  median_household_income: 72589
  poverty_rate: 12.47
  homeownership_rate: 79.67
  unemployment_rate: 3.29
  median_home_value: 321700
  gini_index: 0.4787
  vacancy_rate: 36.33
  race_white: 11975
  race_black: 1623
  race_asian: 132
  race_native: 28
  hispanic: 705
  bachelors_plus: 5583
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/va/districts/senate/11"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/va/districts/house/53"
    rel: in-district
    area_weight: 0.7176
  - to: "us/states/va/districts/house/55"
    rel: in-district
    area_weight: 0.282
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Nelson County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14732 |
| Under 18 | 2564 |
| 18–64 | 7809 |
| 65+ | 4359 |
| Median household income | 72589 |
| Poverty rate | 12.47 |
| Homeownership rate | 79.67 |
| Unemployment rate | 3.29 |
| Median home value | 321700 |
| Gini index | 0.4787 |
| Vacancy rate | 36.33 |
| White | 11975 |
| Black | 1623 |
| Asian | 132 |
| Native | 28 |
| Hispanic/Latino | 705 |
| Bachelor's or higher | 5583 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 11](/us/states/va/districts/senate/11.md) — 100% (state senate)
- [VA House District 53](/us/states/va/districts/house/53.md) — 72% (state house)
- [VA House District 55](/us/states/va/districts/house/55.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
