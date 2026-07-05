---
type: Jurisdiction
title: "Arlington County, VA"
classification: county
fips: "51013"
state: "VA"
demographics:
  population: 236254
  population_under_18: 42601
  population_18_64: 165530
  population_65_plus: 28123
  median_household_income: 142114
  poverty_rate: 7.39
  homeownership_rate: 41.26
  unemployment_rate: 3.3
  median_home_value: 895000
  gini_index: 0.4604
  vacancy_rate: 8.15
  race_white: 142640
  race_black: 22327
  race_asian: 24923
  race_native: 1476
  hispanic: 37572
  bachelors_plus: 206673
districts:
  - to: "us/states/va/districts/08"
    rel: in-district
    area_weight: 0.9928
  - to: "us/states/va/districts/senate/40"
    rel: in-district
    area_weight: 0.8709
  - to: "us/states/va/districts/senate/39"
    rel: in-district
    area_weight: 0.1239
  - to: "us/states/va/districts/house/1"
    rel: in-district
    area_weight: 0.444
  - to: "us/states/va/districts/house/2"
    rel: in-district
    area_weight: 0.3342
  - to: "us/states/va/districts/house/3"
    rel: in-district
    area_weight: 0.2164
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Arlington County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 236254 |
| Under 18 | 42601 |
| 18–64 | 165530 |
| 65+ | 28123 |
| Median household income | 142114 |
| Poverty rate | 7.39 |
| Homeownership rate | 41.26 |
| Unemployment rate | 3.3 |
| Median home value | 895000 |
| Gini index | 0.4604 |
| Vacancy rate | 8.15 |
| White | 142640 |
| Black | 22327 |
| Asian | 24923 |
| Native | 1476 |
| Hispanic/Latino | 37572 |
| Bachelor's or higher | 206673 |

## Districts

- [VA-08](/us/states/va/districts/08.md) — 99% (congressional)
- [VA Senate District 40](/us/states/va/districts/senate/40.md) — 87% (state senate)
- [VA Senate District 39](/us/states/va/districts/senate/39.md) — 12% (state senate)
- [VA House District 1](/us/states/va/districts/house/1.md) — 44% (state house)
- [VA House District 2](/us/states/va/districts/house/2.md) — 33% (state house)
- [VA House District 3](/us/states/va/districts/house/3.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
