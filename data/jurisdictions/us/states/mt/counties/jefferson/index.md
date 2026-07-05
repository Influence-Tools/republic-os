---
type: Jurisdiction
title: "Jefferson County, MT"
classification: county
fips: "30043"
state: "MT"
demographics:
  population: 12774
  population_under_18: 2555
  population_18_64: 7258
  population_65_plus: 2961
  median_household_income: 95490
  poverty_rate: 5.72
  homeownership_rate: 84.19
  unemployment_rate: 4.19
  median_home_value: 446900
  gini_index: 0.4486
  vacancy_rate: 7.6
  race_white: 11717
  race_black: 4
  race_asian: 50
  race_native: 188
  hispanic: 380
  bachelors_plus: 4203
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/mt/districts/senate/38"
    rel: in-district
    area_weight: 0.934
  - to: "us/states/mt/districts/senate/35"
    rel: in-district
    area_weight: 0.0624
  - to: "us/states/mt/districts/house/75"
    rel: in-district
    area_weight: 0.934
  - to: "us/states/mt/districts/house/69"
    rel: in-district
    area_weight: 0.0624
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Jefferson County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12774 |
| Under 18 | 2555 |
| 18–64 | 7258 |
| 65+ | 2961 |
| Median household income | 95490 |
| Poverty rate | 5.72 |
| Homeownership rate | 84.19 |
| Unemployment rate | 4.19 |
| Median home value | 446900 |
| Gini index | 0.4486 |
| Vacancy rate | 7.6 |
| White | 11717 |
| Black | 4 |
| Asian | 50 |
| Native | 188 |
| Hispanic/Latino | 380 |
| Bachelor's or higher | 4203 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 38](/us/states/mt/districts/senate/38.md) — 93% (state senate)
- [MT Senate District 35](/us/states/mt/districts/senate/35.md) — 6% (state senate)
- [MT House District 75](/us/states/mt/districts/house/75.md) — 93% (state house)
- [MT House District 69](/us/states/mt/districts/house/69.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
