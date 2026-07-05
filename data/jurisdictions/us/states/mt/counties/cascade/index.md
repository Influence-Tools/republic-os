---
type: Jurisdiction
title: "Cascade County, MT"
classification: county
fips: "30013"
state: "MT"
demographics:
  population: 84606
  population_under_18: 18862
  population_18_64: 49130
  population_65_plus: 16614
  median_household_income: 67690
  poverty_rate: 13.06
  homeownership_rate: 68.53
  unemployment_rate: 3.3
  median_home_value: 265300
  gini_index: 0.4552
  vacancy_rate: 9.83
  race_white: 70806
  race_black: 1108
  race_asian: 924
  race_native: 2852
  hispanic: 4470
  bachelors_plus: 22656
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/13"
    rel: in-district
    area_weight: 0.7419
  - to: "us/states/mt/districts/senate/39"
    rel: in-district
    area_weight: 0.2442
  - to: "us/states/mt/districts/senate/11"
    rel: in-district
    area_weight: 0.0077
  - to: "us/states/mt/districts/house/25"
    rel: in-district
    area_weight: 0.525
  - to: "us/states/mt/districts/house/78"
    rel: in-district
    area_weight: 0.2442
  - to: "us/states/mt/districts/house/26"
    rel: in-district
    area_weight: 0.2169
  - to: "us/states/mt/districts/house/22"
    rel: in-district
    area_weight: 0.0055
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Cascade County, MT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 84606 |
| Under 18 | 18862 |
| 18–64 | 49130 |
| 65+ | 16614 |
| Median household income | 67690 |
| Poverty rate | 13.06 |
| Homeownership rate | 68.53 |
| Unemployment rate | 3.3 |
| Median home value | 265300 |
| Gini index | 0.4552 |
| Vacancy rate | 9.83 |
| White | 70806 |
| Black | 1108 |
| Asian | 924 |
| Native | 2852 |
| Hispanic/Latino | 4470 |
| Bachelor's or higher | 22656 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 13](/us/states/mt/districts/senate/13.md) — 74% (state senate)
- [MT Senate District 39](/us/states/mt/districts/senate/39.md) — 24% (state senate)
- [MT Senate District 11](/us/states/mt/districts/senate/11.md) — 1% (state senate)
- [MT House District 25](/us/states/mt/districts/house/25.md) — 52% (state house)
- [MT House District 78](/us/states/mt/districts/house/78.md) — 24% (state house)
- [MT House District 26](/us/states/mt/districts/house/26.md) — 22% (state house)
- [MT House District 22](/us/states/mt/districts/house/22.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
