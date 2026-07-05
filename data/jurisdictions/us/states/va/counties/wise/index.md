---
type: Jurisdiction
title: "Wise County, VA"
classification: county
fips: "51195"
state: "VA"
demographics:
  population: 35448
  population_under_18: 7592
  population_18_64: 11463
  population_65_plus: 16393
  median_household_income: 52943
  poverty_rate: 17.23
  homeownership_rate: 74.2
  unemployment_rate: 8.22
  median_home_value: 118600
  gini_index: 0.4178
  vacancy_rate: 16.37
  race_white: 31982
  race_black: 1724
  race_asian: 112
  race_native: 102
  hispanic: 509
  bachelors_plus: 5497
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/va/districts/senate/6"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/va/districts/house/45"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Wise County, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35448 |
| Under 18 | 7592 |
| 18–64 | 11463 |
| 65+ | 16393 |
| Median household income | 52943 |
| Poverty rate | 17.23 |
| Homeownership rate | 74.2 |
| Unemployment rate | 8.22 |
| Median home value | 118600 |
| Gini index | 0.4178 |
| Vacancy rate | 16.37 |
| White | 31982 |
| Black | 1724 |
| Asian | 112 |
| Native | 102 |
| Hispanic/Latino | 509 |
| Bachelor's or higher | 5497 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 6](/us/states/va/districts/senate/6.md) — 100% (state senate)
- [VA House District 45](/us/states/va/districts/house/45.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
