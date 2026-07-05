---
type: Jurisdiction
title: "Frederick County, VA"
classification: county
fips: "51069"
state: "VA"
demographics:
  population: 95008
  population_under_18: 21524
  population_18_64: 55653
  population_65_plus: 17831
  median_household_income: 97606
  poverty_rate: 6.81
  homeownership_rate: 79.32
  unemployment_rate: 4.24
  median_home_value: 386000
  gini_index: 0.4139
  vacancy_rate: 5.1
  race_white: 75587
  race_black: 4235
  race_asian: 1910
  race_native: 554
  hispanic: 11843
  bachelors_plus: 29727
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/va/districts/senate/1"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/va/districts/house/32"
    rel: in-district
    area_weight: 0.8227
  - to: "us/states/va/districts/house/31"
    rel: in-district
    area_weight: 0.1765
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Frederick County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 95008 |
| Under 18 | 21524 |
| 18–64 | 55653 |
| 65+ | 17831 |
| Median household income | 97606 |
| Poverty rate | 6.81 |
| Homeownership rate | 79.32 |
| Unemployment rate | 4.24 |
| Median home value | 386000 |
| Gini index | 0.4139 |
| Vacancy rate | 5.1 |
| White | 75587 |
| Black | 4235 |
| Asian | 1910 |
| Native | 554 |
| Hispanic/Latino | 11843 |
| Bachelor's or higher | 29727 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 1](/us/states/va/districts/senate/1.md) — 100% (state senate)
- [VA House District 32](/us/states/va/districts/house/32.md) — 82% (state house)
- [VA House District 31](/us/states/va/districts/house/31.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
