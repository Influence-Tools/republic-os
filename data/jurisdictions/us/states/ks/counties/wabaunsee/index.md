---
type: Jurisdiction
title: "Wabaunsee County, KS"
classification: county
fips: "20197"
state: "KS"
demographics:
  population: 7009
  population_under_18: 1593
  population_18_64: 3902
  population_65_plus: 1514
  median_household_income: 76908
  poverty_rate: 8.49
  homeownership_rate: 81.07
  unemployment_rate: 4.35
  median_home_value: 177300
  gini_index: 0.3849
  vacancy_rate: 14.41
  race_white: 6399
  race_black: 17
  race_asian: 28
  race_native: 6
  hispanic: 335
  bachelors_plus: 1619
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/ks/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ks/districts/house/51"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Wabaunsee County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7009 |
| Under 18 | 1593 |
| 18–64 | 3902 |
| 65+ | 1514 |
| Median household income | 76908 |
| Poverty rate | 8.49 |
| Homeownership rate | 81.07 |
| Unemployment rate | 4.35 |
| Median home value | 177300 |
| Gini index | 0.3849 |
| Vacancy rate | 14.41 |
| White | 6399 |
| Black | 17 |
| Asian | 28 |
| Native | 6 |
| Hispanic/Latino | 335 |
| Bachelor's or higher | 1619 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 20](/us/states/ks/districts/senate/20.md) — 100% (state senate)
- [KS House District 51](/us/states/ks/districts/house/51.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
