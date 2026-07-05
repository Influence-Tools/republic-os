---
type: Jurisdiction
title: "Rappahannock County, VA"
classification: county
fips: "51157"
state: "VA"
demographics:
  population: 7427
  population_under_18: 1274
  population_18_64: 4085
  population_65_plus: 2068
  median_household_income: 83380
  poverty_rate: 10.26
  homeownership_rate: 73.4
  unemployment_rate: 9.2
  median_home_value: 506400
  gini_index: 0.5007
  vacancy_rate: 22.77
  race_white: 6161
  race_black: 267
  race_asian: 14
  race_native: 34
  hispanic: 358
  bachelors_plus: 2670
districts:
  - to: "us/states/va/districts/10"
    rel: in-district
    area_weight: 0.9917
  - to: "us/states/va/districts/senate/28"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/va/districts/house/61"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Rappahannock County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7427 |
| Under 18 | 1274 |
| 18–64 | 4085 |
| 65+ | 2068 |
| Median household income | 83380 |
| Poverty rate | 10.26 |
| Homeownership rate | 73.4 |
| Unemployment rate | 9.2 |
| Median home value | 506400 |
| Gini index | 0.5007 |
| Vacancy rate | 22.77 |
| White | 6161 |
| Black | 267 |
| Asian | 14 |
| Native | 34 |
| Hispanic/Latino | 358 |
| Bachelor's or higher | 2670 |

## Districts

- [VA-10](/us/states/va/districts/10.md) — 99% (congressional)
- [VA Senate District 28](/us/states/va/districts/senate/28.md) — 100% (state senate)
- [VA House District 61](/us/states/va/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
