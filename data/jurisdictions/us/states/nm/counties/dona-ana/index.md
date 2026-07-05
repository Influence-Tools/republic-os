---
type: Jurisdiction
title: "Doña Ana County, NM"
classification: county
fips: "35013"
state: "NM"
demographics:
  population: 224266
  population_under_18: 51915
  population_18_64: 134120
  population_65_plus: 38231
  median_household_income: 56848
  poverty_rate: 21.32
  homeownership_rate: 65.47
  unemployment_rate: 6.76
  median_home_value: 220800
  gini_index: 0.4781
  vacancy_rate: 8.16
  race_white: 91627
  race_black: 3907
  race_asian: 2728
  race_native: 2749
  hispanic: 152201
  bachelors_plus: 63773
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/senate/35"
    rel: in-district
    area_weight: 0.4202
  - to: "us/states/nm/districts/senate/38"
    rel: in-district
    area_weight: 0.3221
  - to: "us/states/nm/districts/senate/37"
    rel: in-district
    area_weight: 0.1053
  - to: "us/states/nm/districts/senate/36"
    rel: in-district
    area_weight: 0.1014
  - to: "us/states/nm/districts/senate/31"
    rel: in-district
    area_weight: 0.051
  - to: "us/states/nm/districts/house/38"
    rel: in-district
    area_weight: 0.3144
  - to: "us/states/nm/districts/house/34"
    rel: in-district
    area_weight: 0.2808
  - to: "us/states/nm/districts/house/36"
    rel: in-district
    area_weight: 0.1175
  - to: "us/states/nm/districts/house/53"
    rel: in-district
    area_weight: 0.1132
  - to: "us/states/nm/districts/house/32"
    rel: in-district
    area_weight: 0.0844
  - to: "us/states/nm/districts/house/33"
    rel: in-district
    area_weight: 0.0473
  - to: "us/states/nm/districts/house/52"
    rel: in-district
    area_weight: 0.0363
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Doña Ana County, NM

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 224266 |
| Under 18 | 51915 |
| 18–64 | 134120 |
| 65+ | 38231 |
| Median household income | 56848 |
| Poverty rate | 21.32 |
| Homeownership rate | 65.47 |
| Unemployment rate | 6.76 |
| Median home value | 220800 |
| Gini index | 0.4781 |
| Vacancy rate | 8.16 |
| White | 91627 |
| Black | 3907 |
| Asian | 2728 |
| Native | 2749 |
| Hispanic/Latino | 152201 |
| Bachelor's or higher | 63773 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 100% (congressional)
- [NM Senate District 35](/us/states/nm/districts/senate/35.md) — 42% (state senate)
- [NM Senate District 38](/us/states/nm/districts/senate/38.md) — 32% (state senate)
- [NM Senate District 37](/us/states/nm/districts/senate/37.md) — 11% (state senate)
- [NM Senate District 36](/us/states/nm/districts/senate/36.md) — 10% (state senate)
- [NM Senate District 31](/us/states/nm/districts/senate/31.md) — 5% (state senate)
- [NM House District 38](/us/states/nm/districts/house/38.md) — 31% (state house)
- [NM House District 34](/us/states/nm/districts/house/34.md) — 28% (state house)
- [NM House District 36](/us/states/nm/districts/house/36.md) — 12% (state house)
- [NM House District 53](/us/states/nm/districts/house/53.md) — 11% (state house)
- [NM House District 32](/us/states/nm/districts/house/32.md) — 8% (state house)
- [NM House District 33](/us/states/nm/districts/house/33.md) — 5% (state house)
- [NM House District 52](/us/states/nm/districts/house/52.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
