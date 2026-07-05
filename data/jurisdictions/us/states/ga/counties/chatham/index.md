---
type: Jurisdiction
title: "Chatham County, GA"
classification: county
fips: "13051"
state: "GA"
demographics:
  population: 300879
  population_under_18: 62225
  population_18_64: 188278
  population_65_plus: 50376
  median_household_income: 71097
  poverty_rate: 14.33
  homeownership_rate: 56.75
  unemployment_rate: 5.94
  median_home_value: 302700
  gini_index: 0.4721
  vacancy_rate: 12.47
  race_white: 141221
  race_black: 117105
  race_asian: 9384
  race_native: 984
  hispanic: 24958
  bachelors_plus: 110221
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.7811
  - to: "us/states/ga/districts/senate/1"
    rel: in-district
    area_weight: 0.4872
  - to: "us/states/ga/districts/senate/2"
    rel: in-district
    area_weight: 0.244
  - to: "us/states/ga/districts/senate/4"
    rel: in-district
    area_weight: 0.0519
  - to: "us/states/ga/districts/house/166"
    rel: in-district
    area_weight: 0.338
  - to: "us/states/ga/districts/house/164"
    rel: in-district
    area_weight: 0.1624
  - to: "us/states/ga/districts/house/161"
    rel: in-district
    area_weight: 0.088
  - to: "us/states/ga/districts/house/162"
    rel: in-district
    area_weight: 0.0797
  - to: "us/states/ga/districts/house/165"
    rel: in-district
    area_weight: 0.0594
  - to: "us/states/ga/districts/house/163"
    rel: in-district
    area_weight: 0.0557
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Chatham County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 300879 |
| Under 18 | 62225 |
| 18–64 | 188278 |
| 65+ | 50376 |
| Median household income | 71097 |
| Poverty rate | 14.33 |
| Homeownership rate | 56.75 |
| Unemployment rate | 5.94 |
| Median home value | 302700 |
| Gini index | 0.4721 |
| Vacancy rate | 12.47 |
| White | 141221 |
| Black | 117105 |
| Asian | 9384 |
| Native | 984 |
| Hispanic/Latino | 24958 |
| Bachelor's or higher | 110221 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 78% (congressional)
- [GA Senate District 1](/us/states/ga/districts/senate/1.md) — 49% (state senate)
- [GA Senate District 2](/us/states/ga/districts/senate/2.md) — 24% (state senate)
- [GA Senate District 4](/us/states/ga/districts/senate/4.md) — 5% (state senate)
- [GA House District 166](/us/states/ga/districts/house/166.md) — 34% (state house)
- [GA House District 164](/us/states/ga/districts/house/164.md) — 16% (state house)
- [GA House District 161](/us/states/ga/districts/house/161.md) — 9% (state house)
- [GA House District 162](/us/states/ga/districts/house/162.md) — 8% (state house)
- [GA House District 165](/us/states/ga/districts/house/165.md) — 6% (state house)
- [GA House District 163](/us/states/ga/districts/house/163.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
