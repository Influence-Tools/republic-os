---
type: Jurisdiction
title: "Rensselaer County, NY"
classification: county
fips: "36083"
state: "NY"
demographics:
  population: 160332
  population_under_18: 30562
  population_18_64: 100440
  population_65_plus: 29330
  median_household_income: 87915
  poverty_rate: 11.82
  homeownership_rate: 64.77
  unemployment_rate: 5.3
  median_home_value: 258400
  gini_index: 0.428
  vacancy_rate: 10.54
  race_white: 128235
  race_black: 11173
  race_asian: 5164
  race_native: 250
  hispanic: 9863
  bachelors_plus: 60326
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.6729
  - to: "us/states/ny/districts/20"
    rel: in-district
    area_weight: 0.3266
  - to: "us/states/ny/districts/senate/43"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ny/districts/house/107"
    rel: in-district
    area_weight: 0.913
  - to: "us/states/ny/districts/house/108"
    rel: in-district
    area_weight: 0.0867
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Rensselaer County, NY

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 160332 |
| Under 18 | 30562 |
| 18–64 | 100440 |
| 65+ | 29330 |
| Median household income | 87915 |
| Poverty rate | 11.82 |
| Homeownership rate | 64.77 |
| Unemployment rate | 5.3 |
| Median home value | 258400 |
| Gini index | 0.428 |
| Vacancy rate | 10.54 |
| White | 128235 |
| Black | 11173 |
| Asian | 5164 |
| Native | 250 |
| Hispanic/Latino | 9863 |
| Bachelor's or higher | 60326 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 67% (congressional)
- [NY-20](/us/states/ny/districts/20.md) — 33% (congressional)
- [NY Senate District 43](/us/states/ny/districts/senate/43.md) — 100% (state senate)
- [NY House District 107](/us/states/ny/districts/house/107.md) — 91% (state house)
- [NY House District 108](/us/states/ny/districts/house/108.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
